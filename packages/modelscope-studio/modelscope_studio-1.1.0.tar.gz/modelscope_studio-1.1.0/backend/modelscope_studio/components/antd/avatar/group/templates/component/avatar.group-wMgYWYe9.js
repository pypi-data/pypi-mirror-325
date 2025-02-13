import { i as ae, a as M, r as ce, g as ue, w as O, d as de, b as T } from "./Index-kA5OrFDq.js";
const b = window.ms_globals.React, Q = window.ms_globals.React.useMemo, Z = window.ms_globals.React.useState, $ = window.ms_globals.React.useEffect, ie = window.ms_globals.React.forwardRef, le = window.ms_globals.React.useRef, W = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, pe = window.ms_globals.antd.Avatar;
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
var U = NaN, xe = /^[-+]0x[0-9a-f]+$/i, ve = /^0b[01]+$/i, be = /^0o[0-7]+$/i, ye = parseInt;
function B(e) {
  if (typeof e == "number")
    return e;
  if (ae(e))
    return U;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = he(e);
  var o = ve.test(e);
  return o || be.test(e) ? ye(e.slice(2), o ? 2 : 8) : xe.test(e) ? U : +e;
}
var A = function() {
  return ce.Date.now();
}, we = "Expected a function", Ee = Math.max, Ie = Math.min;
function Ce(e, t, o) {
  var i, s, n, r, l, c, m = 0, _ = !1, a = !1, h = !0;
  if (typeof e != "function")
    throw new TypeError(we);
  t = B(t) || 0, M(o) && (_ = !!o.leading, a = "maxWait" in o, n = a ? Ee(B(o.maxWait) || 0, t) : n, h = "trailing" in o ? !!o.trailing : h);
  function d(f) {
    var v = i, R = s;
    return i = s = void 0, m = f, r = e.apply(R, v), r;
  }
  function w(f) {
    return m = f, l = setTimeout(x, t), _ ? d(f) : r;
  }
  function p(f) {
    var v = f - c, R = f - m, G = t - v;
    return a ? Ie(G, n - R) : G;
  }
  function g(f) {
    var v = f - c, R = f - m;
    return c === void 0 || v >= t || v < 0 || a && R >= n;
  }
  function x() {
    var f = A();
    if (g(f))
      return E(f);
    l = setTimeout(x, p(f));
  }
  function E(f) {
    return l = void 0, h && i ? d(f) : (i = s = void 0, r);
  }
  function I() {
    l !== void 0 && clearTimeout(l), m = 0, i = c = s = l = void 0;
  }
  function u() {
    return l === void 0 ? r : E(A());
  }
  function C() {
    var f = A(), v = g(f);
    if (i = arguments, s = this, c = f, v) {
      if (l === void 0)
        return w(c);
      if (a)
        return clearTimeout(l), l = setTimeout(x, t), d(c);
    }
    return l === void 0 && (l = setTimeout(x, t)), r;
  }
  return C.cancel = I, C.flush = u, C;
}
var ee = {
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
var Se = b, Re = Symbol.for("react.element"), Te = Symbol.for("react.fragment"), Oe = Object.prototype.hasOwnProperty, ke = Se.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
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
P.Fragment = Te;
P.jsx = te;
P.jsxs = te;
ee.exports = P;
var y = ee.exports;
const {
  SvelteComponent: Pe,
  assign: z,
  binding_callbacks: H,
  check_outros: Ae,
  children: ne,
  claim_element: re,
  claim_space: je,
  component_subscribe: K,
  compute_slots: Ne,
  create_slot: We,
  detach: S,
  element: oe,
  empty: V,
  exclude_internal_props: q,
  get_all_dirty_from_scope: Me,
  get_slot_changes: De,
  group_outros: Fe,
  init: Ge,
  insert_hydration: k,
  safe_not_equal: Ue,
  set_custom_element_data: se,
  space: Be,
  transition_in: L,
  transition_out: D,
  update_slot_base: ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: He,
  getContext: Ke,
  onDestroy: Ve,
  setContext: qe
} = window.__gradio__svelte__internal;
function J(e) {
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
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
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
      o || (L(s, n), o = !0);
    },
    o(n) {
      D(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function Je(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && J(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), o = Be(), n && n.c(), i = V(), this.h();
    },
    l(r) {
      t = re(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(S), o = je(r), n && n.l(r), i = V(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, o, l), n && n.m(r, l), k(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && L(n, 1)) : (n = J(r), n.c(), L(n, 1), n.m(i.parentNode, i)) : n && (Fe(), D(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      s || (L(n), s = !0);
    },
    o(r) {
      D(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(i)), e[8](null), n && n.d(r);
    }
  };
}
function X(e) {
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
  const l = Ne(n);
  let {
    svelteInit: c
  } = t;
  const m = O(X(t)), _ = O();
  K(e, _, (u) => o(0, i = u));
  const a = O();
  K(e, a, (u) => o(1, s = u));
  const h = [], d = Ke("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: p,
    subSlotIndex: g
  } = ue() || {}, x = c({
    parent: d,
    props: m,
    target: _,
    slot: a,
    slotKey: w,
    slotIndex: p,
    subSlotIndex: g,
    onDestroy(u) {
      h.push(u);
    }
  });
  qe("$$ms-gr-react-wrapper", x), He(() => {
    m.set(X(t));
  }), Ve(() => {
    h.forEach((u) => u());
  });
  function E(u) {
    H[u ? "unshift" : "push"](() => {
      i = u, _.set(i);
    });
  }
  function I(u) {
    H[u ? "unshift" : "push"](() => {
      s = u, a.set(s);
    });
  }
  return e.$$set = (u) => {
    o(17, t = z(z({}, t), q(u))), "svelteInit" in u && o(5, c = u.svelteInit), "$$scope" in u && o(6, r = u.$$scope);
  }, t = q(t), [i, s, _, a, l, c, r, n, E, I];
}
class Ye extends Pe {
  constructor(t) {
    super(), Ge(this, t, Xe, Je, Ue, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, j = window.ms_globals.tree;
function Qe(e, t = {}) {
  function o(i) {
    const s = O(), n = new Ye({
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
          }, c = r.parent ?? j;
          return c.nodes = [...c.nodes, l], Y({
            createPortal: W,
            node: j
          }), r.onDestroy(() => {
            c.nodes = c.nodes.filter((m) => m.svelteInstance !== s), Y({
              createPortal: W,
              node: j
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
  const [t, o] = Z(() => T(e));
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
function F(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = b.Children.toArray(e._reactElement.props.children).map((n) => {
      if (b.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = F(n.props.el);
        return b.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...b.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(W(b.cloneElement(e._reactElement, {
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
      useCapture: c
    }) => {
      o.addEventListener(l, r, c);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = F(n);
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
const N = ie(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = le(), [l, c] = Z([]), {
    forceClone: m
  } = fe(), _ = m ? !0 : t;
  return $(() => {
    var w;
    if (!r.current || !e)
      return;
    let a = e;
    function h() {
      let p = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (p = a.children[0], p.tagName.toLowerCase() === "react-portal-target" && p.children[0] && (p = p.children[0])), rt(n, p), o && p.classList.add(...o.split(" ")), i) {
        const g = tt(i);
        Object.keys(g).forEach((x) => {
          p.style[x] = g[x];
        });
      }
    }
    let d = null;
    if (_ && window.MutationObserver) {
      let p = function() {
        var I, u, C;
        (I = r.current) != null && I.contains(a) && ((u = r.current) == null || u.removeChild(a));
        const {
          portals: x,
          clonedElement: E
        } = F(e);
        a = E, c(x), a.style.display = "contents", h(), (C = r.current) == null || C.appendChild(a);
      };
      p();
      const g = Ce(() => {
        p(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      d = new window.MutationObserver(g), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", h(), (w = r.current) == null || w.appendChild(a);
    return () => {
      var p, g;
      a.style.display = "", (p = r.current) != null && p.contains(a) && ((g = r.current) == null || g.removeChild(a)), d == null || d.disconnect();
    };
  }, [e, _, o, i, n, s]), b.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ot(e, t) {
  const o = Q(() => b.Children.toArray(e.originalChildren || e).filter((n) => n.props.node && !n.props.node.ignore && (!n.props.nodeSlotKey || t)).sort((n, r) => {
    if (n.props.node.slotIndex && r.props.node.slotIndex) {
      const l = T(n.props.node.slotIndex) || 0, c = T(r.props.node.slotIndex) || 0;
      return l - c === 0 && n.props.node.subSlotIndex && r.props.node.subSlotIndex ? (T(n.props.node.subSlotIndex) || 0) - (T(r.props.node.subSlotIndex) || 0) : l - c;
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
  var s, n, r, l, c, m, _, a;
  const i = ot(t);
  return /* @__PURE__ */ y.jsx(y.Fragment, {
    children: /* @__PURE__ */ y.jsxs(pe.Group, {
      ...o,
      max: {
        ...o.max,
        count: typeof ((s = o.max) == null ? void 0 : s.count) == "number" ? (
          // children render
          o.max.count + 1
        ) : (n = o.max) == null ? void 0 : n.count,
        popover: e["max.popover.title"] || e["max.popover.content"] ? {
          ...((l = o.max) == null ? void 0 : l.popover) || {},
          title: e["max.popover.title"] ? /* @__PURE__ */ y.jsx(N, {
            slot: e["max.popover.title"]
          }) : (m = (c = o.max) == null ? void 0 : c.popover) == null ? void 0 : m.title,
          content: e["max.popover.content"] ? /* @__PURE__ */ y.jsx(N, {
            slot: e["max.popover.content"]
          }) : (a = (_ = o.max) == null ? void 0 : _.popover) == null ? void 0 : a.content
        } : (r = o.max) == null ? void 0 : r.popover
      },
      children: [/* @__PURE__ */ y.jsx("div", {
        style: {
          display: "none"
        },
        children: t
      }), i.map((h, d) => /* @__PURE__ */ y.jsx(N, {
        slot: h
      }, d))]
    })
  });
});
export {
  it as AvatarGroup,
  it as default
};
