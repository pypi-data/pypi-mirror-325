import { i as le, a as W, r as ae, g as ce, w as O, d as ue, b as T } from "./Index-DoCSX7i3.js";
const x = window.ms_globals.React, Y = window.ms_globals.React.useMemo, Q = window.ms_globals.React.useState, Z = window.ms_globals.React.useEffect, se = window.ms_globals.React.forwardRef, ie = window.ms_globals.React.useRef, j = window.ms_globals.ReactDOM.createPortal, de = window.ms_globals.internalContext.useContextPropsContext, fe = window.ms_globals.antd.Space;
var pe = /\s/;
function me(e) {
  for (var t = e.length; t-- && pe.test(e.charAt(t)); )
    ;
  return t;
}
var _e = /^\s+/;
function ge(e) {
  return e && e.slice(0, me(e) + 1).replace(_e, "");
}
var U = NaN, he = /^[-+]0x[0-9a-f]+$/i, be = /^0b[01]+$/i, ye = /^0o[0-7]+$/i, xe = parseInt;
function B(e) {
  if (typeof e == "number")
    return e;
  if (le(e))
    return U;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ge(e);
  var o = be.test(e);
  return o || ye.test(e) ? xe(e.slice(2), o ? 2 : 8) : he.test(e) ? U : +e;
}
var A = function() {
  return ae.Date.now();
}, we = "Expected a function", Ee = Math.max, ve = Math.min;
function Ie(e, t, o) {
  var i, s, n, r, l, u, m = 0, h = !1, a = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(we);
  t = B(t) || 0, W(o) && (h = !!o.leading, a = "maxWait" in o, n = a ? Ee(B(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function p(d) {
    var y = i, S = s;
    return i = s = void 0, m = d, r = e.apply(S, y), r;
  }
  function w(d) {
    return m = d, l = setTimeout(g, t), h ? p(d) : r;
  }
  function f(d) {
    var y = d - u, S = d - m, F = t - y;
    return a ? ve(F, n - S) : F;
  }
  function _(d) {
    var y = d - u, S = d - m;
    return u === void 0 || y >= t || y < 0 || a && S >= n;
  }
  function g() {
    var d = A();
    if (_(d))
      return E(d);
    l = setTimeout(g, f(d));
  }
  function E(d) {
    return l = void 0, b && i ? p(d) : (i = s = void 0, r);
  }
  function v() {
    l !== void 0 && clearTimeout(l), m = 0, i = u = s = l = void 0;
  }
  function c() {
    return l === void 0 ? r : E(A());
  }
  function I() {
    var d = A(), y = _(d);
    if (i = arguments, s = this, u = d, y) {
      if (l === void 0)
        return w(u);
      if (a)
        return clearTimeout(l), l = setTimeout(g, t), p(u);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return I.cancel = v, I.flush = c, I;
}
var $ = {
  exports: {}
}, P = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ce = x, Se = Symbol.for("react.element"), Re = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, Oe = Ce.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ke = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ee(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Te.call(t, i) && !ke.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Se,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Oe.current
  };
}
P.Fragment = Re;
P.jsx = ee;
P.jsxs = ee;
$.exports = P;
var R = $.exports;
const {
  SvelteComponent: Le,
  assign: z,
  binding_callbacks: G,
  check_outros: Pe,
  children: te,
  claim_element: ne,
  claim_space: Ae,
  component_subscribe: H,
  compute_slots: Ne,
  create_slot: je,
  detach: C,
  element: re,
  empty: K,
  exclude_internal_props: V,
  get_all_dirty_from_scope: We,
  get_slot_changes: Me,
  group_outros: De,
  init: Fe,
  insert_hydration: k,
  safe_not_equal: Ue,
  set_custom_element_data: oe,
  space: Be,
  transition_in: L,
  transition_out: M,
  update_slot_base: ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ge,
  getContext: He,
  onDestroy: Ke,
  setContext: Ve
} = window.__gradio__svelte__internal;
function q(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = je(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = re("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = ne(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = te(t);
      s && s.l(r), r.forEach(C), this.h();
    },
    h() {
      oe(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && ze(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? Me(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : We(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (L(s, n), o = !0);
    },
    o(n) {
      M(s, n), o = !1;
    },
    d(n) {
      n && C(t), s && s.d(n), e[9](null);
    }
  };
}
function qe(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = re("react-portal-target"), o = Be(), n && n.c(), i = K(), this.h();
    },
    l(r) {
      t = ne(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), te(t).forEach(C), o = Ae(r), n && n.l(r), i = K(), this.h();
    },
    h() {
      oe(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, o, l), n && n.m(r, l), k(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && L(n, 1)) : (n = q(r), n.c(), L(n, 1), n.m(i.parentNode, i)) : n && (De(), M(n, 1, 1, () => {
        n = null;
      }), Pe());
    },
    i(r) {
      s || (L(n), s = !0);
    },
    o(r) {
      M(n), s = !1;
    },
    d(r) {
      r && (C(t), C(o), C(i)), e[8](null), n && n.d(r);
    }
  };
}
function J(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Je(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ne(n);
  let {
    svelteInit: u
  } = t;
  const m = O(J(t)), h = O();
  H(e, h, (c) => o(0, i = c));
  const a = O();
  H(e, a, (c) => o(1, s = c));
  const b = [], p = He("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _
  } = ce() || {}, g = u({
    parent: p,
    props: m,
    target: h,
    slot: a,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(c) {
      b.push(c);
    }
  });
  Ve("$$ms-gr-react-wrapper", g), Ge(() => {
    m.set(J(t));
  }), Ke(() => {
    b.forEach((c) => c());
  });
  function E(c) {
    G[c ? "unshift" : "push"](() => {
      i = c, h.set(i);
    });
  }
  function v(c) {
    G[c ? "unshift" : "push"](() => {
      s = c, a.set(s);
    });
  }
  return e.$$set = (c) => {
    o(17, t = z(z({}, t), V(c))), "svelteInit" in c && o(5, u = c.svelteInit), "$$scope" in c && o(6, r = c.$$scope);
  }, t = V(t), [i, s, h, a, l, u, r, n, E, v];
}
class Xe extends Le {
  constructor(t) {
    super(), Fe(this, t, Je, qe, Ue, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, N = window.ms_globals.tree;
function Ye(e, t = {}) {
  function o(i) {
    const s = O(), n = new Xe({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? N;
          return u.nodes = [...u.nodes, l], X({
            createPortal: j,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((m) => m.svelteInstance !== s), X({
              createPortal: j,
              node: N
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(o);
    });
  });
}
function Qe(e) {
  const [t, o] = Q(() => T(e));
  return Z(() => {
    let i = !0;
    return e.subscribe((n) => {
      i && (i = !1, n === t) || o(n);
    });
  }, [e]), t;
}
function Ze(e) {
  const t = Y(() => ue(e, (o) => o), [e]);
  return Qe(t);
}
const $e = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function et(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = tt(o, i), t;
  }, {}) : {};
}
function tt(e, t) {
  return typeof t == "number" && !$e.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = x.Children.toArray(e._reactElement.props.children).map((n) => {
      if (x.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = D(n.props.el);
        return x.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...x.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(j(x.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = D(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function nt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const rt = se(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = ie(), [l, u] = Q([]), {
    forceClone: m
  } = de(), h = m ? !0 : t;
  return Z(() => {
    var w;
    if (!r.current || !e)
      return;
    let a = e;
    function b() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), nt(n, f), o && f.classList.add(...o.split(" ")), i) {
        const _ = et(i);
        Object.keys(_).forEach((g) => {
          f.style[g] = _[g];
        });
      }
    }
    let p = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var v, c, I;
        (v = r.current) != null && v.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: g,
          clonedElement: E
        } = D(e);
        a = E, u(g), a.style.display = "contents", b(), (I = r.current) == null || I.appendChild(a);
      };
      f();
      const _ = Ie(() => {
        f(), p == null || p.disconnect(), p == null || p.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      p = new window.MutationObserver(_), p.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", b(), (w = r.current) == null || w.appendChild(a);
    return () => {
      var f, _;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((_ = r.current) == null || _.removeChild(a)), p == null || p.disconnect();
    };
  }, [e, h, o, i, n, s]), x.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ot(e, t) {
  const o = Y(() => x.Children.toArray(e.originalChildren || e).filter((n) => n.props.node && !n.props.node.ignore && (!n.props.nodeSlotKey || t)).sort((n, r) => {
    if (n.props.node.slotIndex && r.props.node.slotIndex) {
      const l = T(n.props.node.slotIndex) || 0, u = T(r.props.node.slotIndex) || 0;
      return l - u === 0 && n.props.node.subSlotIndex && r.props.node.subSlotIndex ? (T(n.props.node.subSlotIndex) || 0) - (T(r.props.node.subSlotIndex) || 0) : l - u;
    }
    return 0;
  }).map((n) => n.props.node.target), [e, t]);
  return Ze(o);
}
const it = Ye(({
  children: e,
  ...t
}) => {
  const o = ot(e);
  return /* @__PURE__ */ R.jsxs(R.Fragment, {
    children: [/* @__PURE__ */ R.jsx("div", {
      style: {
        display: "none"
      },
      children: e
    }), /* @__PURE__ */ R.jsx(fe.Compact, {
      ...t,
      children: o.map((i, s) => /* @__PURE__ */ R.jsx(rt, {
        slot: i
      }, s))
    })]
  });
});
export {
  it as Space,
  it as default
};
