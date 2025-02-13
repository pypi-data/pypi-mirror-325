import { i as ae, a as W, r as ce, g as ue, w as T, d as de, b as R } from "./Index-qRq9kbMc.js";
const y = window.ms_globals.React, Q = window.ms_globals.React.useMemo, Z = window.ms_globals.React.useState, $ = window.ms_globals.React.useEffect, ie = window.ms_globals.React.forwardRef, le = window.ms_globals.React.useRef, j = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, pe = window.ms_globals.antd.List;
var me = /\s/;
function _e(e) {
  for (var t = e.length; t-- && me.test(e.charAt(t)); )
    ;
  return t;
}
var ge = /^\s+/;
function he(e) {
  return e && e.slice(0, _e(e) + 1).replace(ge, "");
}
var U = NaN, be = /^[-+]0x[0-9a-f]+$/i, xe = /^0b[01]+$/i, ye = /^0o[0-7]+$/i, we = parseInt;
function B(e) {
  if (typeof e == "number")
    return e;
  if (ae(e))
    return U;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = he(e);
  var o = xe.test(e);
  return o || ye.test(e) ? we(e.slice(2), o ? 2 : 8) : be.test(e) ? U : +e;
}
var P = function() {
  return ce.Date.now();
}, Ee = "Expected a function", Ie = Math.max, ve = Math.min;
function Ce(e, t, o) {
  var i, s, n, r, l, u, m = 0, h = !1, a = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(Ee);
  t = B(t) || 0, W(o) && (h = !!o.leading, a = "maxWait" in o, n = a ? Ie(B(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function p(d) {
    var x = i, S = s;
    return i = s = void 0, m = d, r = e.apply(S, x), r;
  }
  function w(d) {
    return m = d, l = setTimeout(g, t), h ? p(d) : r;
  }
  function f(d) {
    var x = d - u, S = d - m, F = t - x;
    return a ? ve(F, n - S) : F;
  }
  function _(d) {
    var x = d - u, S = d - m;
    return u === void 0 || x >= t || x < 0 || a && S >= n;
  }
  function g() {
    var d = P();
    if (_(d))
      return E(d);
    l = setTimeout(g, f(d));
  }
  function E(d) {
    return l = void 0, b && i ? p(d) : (i = s = void 0, r);
  }
  function I() {
    l !== void 0 && clearTimeout(l), m = 0, i = u = s = l = void 0;
  }
  function c() {
    return l === void 0 ? r : E(P());
  }
  function v() {
    var d = P(), x = _(d);
    if (i = arguments, s = this, u = d, x) {
      if (l === void 0)
        return w(u);
      if (a)
        return clearTimeout(l), l = setTimeout(g, t), p(u);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return v.cancel = I, v.flush = c, v;
}
var ee = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Se = y, Re = Symbol.for("react.element"), Te = Symbol.for("react.fragment"), Oe = Object.prototype.hasOwnProperty, ke = Se.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Oe.call(t, i) && !Le.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Re,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: ke.current
  };
}
L.Fragment = Te;
L.jsx = te;
L.jsxs = te;
ee.exports = L;
var A = ee.exports;
const {
  SvelteComponent: Pe,
  assign: z,
  binding_callbacks: G,
  check_outros: Ae,
  children: ne,
  claim_element: re,
  claim_space: Ne,
  component_subscribe: H,
  compute_slots: je,
  create_slot: We,
  detach: C,
  element: oe,
  empty: K,
  exclude_internal_props: V,
  get_all_dirty_from_scope: Me,
  get_slot_changes: De,
  group_outros: Fe,
  init: Ue,
  insert_hydration: O,
  safe_not_equal: Be,
  set_custom_element_data: se,
  space: ze,
  transition_in: k,
  transition_out: M,
  update_slot_base: Ge
} = window.__gradio__svelte__internal, {
  beforeUpdate: He,
  getContext: Ke,
  onDestroy: Ve,
  setContext: qe
} = window.__gradio__svelte__internal;
function q(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = We(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ne(t);
      s && s.l(r), r.forEach(C), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Ge(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? De(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Me(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (k(s, n), o = !0);
    },
    o(n) {
      M(s, n), o = !1;
    },
    d(n) {
      n && C(t), s && s.d(n), e[9](null);
    }
  };
}
function Je(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), o = ze(), n && n.c(), i = K(), this.h();
    },
    l(r) {
      t = re(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(C), o = Ne(r), n && n.l(r), i = K(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      O(r, t, l), e[8](t), O(r, o, l), n && n.m(r, l), O(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && k(n, 1)) : (n = q(r), n.c(), k(n, 1), n.m(i.parentNode, i)) : n && (Fe(), M(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      s || (k(n), s = !0);
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
function Xe(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = je(n);
  let {
    svelteInit: u
  } = t;
  const m = T(J(t)), h = T();
  H(e, h, (c) => o(0, i = c));
  const a = T();
  H(e, a, (c) => o(1, s = c));
  const b = [], p = Ke("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _
  } = ue() || {}, g = u({
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
  qe("$$ms-gr-react-wrapper", g), He(() => {
    m.set(J(t));
  }), Ve(() => {
    b.forEach((c) => c());
  });
  function E(c) {
    G[c ? "unshift" : "push"](() => {
      i = c, h.set(i);
    });
  }
  function I(c) {
    G[c ? "unshift" : "push"](() => {
      s = c, a.set(s);
    });
  }
  return e.$$set = (c) => {
    o(17, t = z(z({}, t), V(c))), "svelteInit" in c && o(5, u = c.svelteInit), "$$scope" in c && o(6, r = c.$$scope);
  }, t = V(t), [i, s, h, a, l, u, r, n, E, I];
}
class Ye extends Pe {
  constructor(t) {
    super(), Ue(this, t, Xe, Je, Be, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, N = window.ms_globals.tree;
function Qe(e, t = {}) {
  function o(i) {
    const s = T(), n = new Ye({
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
function Ze(e) {
  const [t, o] = Z(() => R(e));
  return $(() => {
    let i = !0;
    return e.subscribe((n) => {
      i && (i = !1, n === t) || o(n);
    });
  }, [e]), t;
}
function $e(e) {
  const t = Q(() => de(e, (o) => o), [e]);
  return Ze(t);
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = nt(o, i), t;
  }, {}) : {};
}
function nt(e, t) {
  return typeof t == "number" && !et.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = D(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(j(y.cloneElement(e._reactElement, {
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
function rt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Y = ie(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = le(), [l, u] = Z([]), {
    forceClone: m
  } = fe(), h = m ? !0 : t;
  return $(() => {
    var w;
    if (!r.current || !e)
      return;
    let a = e;
    function b() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), o && f.classList.add(...o.split(" ")), i) {
        const _ = tt(i);
        Object.keys(_).forEach((g) => {
          f.style[g] = _[g];
        });
      }
    }
    let p = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var I, c, v;
        (I = r.current) != null && I.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: g,
          clonedElement: E
        } = D(e);
        a = E, u(g), a.style.display = "contents", b(), (v = r.current) == null || v.appendChild(a);
      };
      f();
      const _ = Ce(() => {
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
  }, [e, h, o, i, n, s]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ot(e, t) {
  const o = Q(() => y.Children.toArray(e.originalChildren || e).filter((n) => n.props.node && !n.props.node.ignore && t === n.props.nodeSlotKey).sort((n, r) => {
    if (n.props.node.slotIndex && r.props.node.slotIndex) {
      const l = R(n.props.node.slotIndex) || 0, u = R(r.props.node.slotIndex) || 0;
      return l - u === 0 && n.props.node.subSlotIndex && r.props.node.subSlotIndex ? (R(n.props.node.subSlotIndex) || 0) - (R(r.props.node.subSlotIndex) || 0) : l - u;
    }
    return 0;
  }).map((n) => n.props.node.target), [e, t]);
  return $e(o);
}
const it = Qe(({
  slots: e,
  children: t,
  ...o
}) => {
  const i = ot(t, "actions");
  return /* @__PURE__ */ A.jsx(pe.Item, {
    ...o,
    extra: e.extra ? /* @__PURE__ */ A.jsx(Y, {
      slot: e.extra
    }) : o.extra,
    actions: i.length > 0 ? i.map((s, n) => /* @__PURE__ */ A.jsx(Y, {
      slot: s
    }, n)) : o.actions,
    children: t
  });
});
export {
  it as ListItem,
  it as default
};
