import { i as ie, a as A, r as ae, g as ce, w as O } from "./Index-DElMqvtl.js";
const y = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, le = window.ms_globals.React.createElement, j = window.ms_globals.ReactDOM.createPortal, ue = window.ms_globals.internalContext.useContextPropsContext, M = window.ms_globals.antd.Splitter, de = window.ms_globals.createItemsContext.createItemsContext;
var fe = /\s/;
function me(e) {
  for (var t = e.length; t-- && fe.test(e.charAt(t)); )
    ;
  return t;
}
var pe = /^\s+/;
function _e(e) {
  return e && e.slice(0, me(e) + 1).replace(pe, "");
}
var U = NaN, he = /^[-+]0x[0-9a-f]+$/i, ge = /^0b[01]+$/i, be = /^0o[0-7]+$/i, we = parseInt;
function H(e) {
  if (typeof e == "number")
    return e;
  if (ie(e))
    return U;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = _e(e);
  var o = ge.test(e);
  return o || be.test(e) ? we(e.slice(2), o ? 2 : 8) : he.test(e) ? U : +e;
}
var L = function() {
  return ae.Date.now();
}, ye = "Expected a function", Ee = Math.max, xe = Math.min;
function Ce(e, t, o) {
  var l, s, n, r, i, u, p = 0, g = !1, a = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(ye);
  t = H(t) || 0, A(o) && (g = !!o.leading, a = "maxWait" in o, n = a ? Ee(H(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function m(d) {
    var w = l, S = s;
    return l = s = void 0, p = d, r = e.apply(S, w), r;
  }
  function E(d) {
    return p = d, i = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var w = d - u, S = d - p, F = t - w;
    return a ? xe(F, n - S) : F;
  }
  function _(d) {
    var w = d - u, S = d - p;
    return u === void 0 || w >= t || w < 0 || a && S >= n;
  }
  function h() {
    var d = L();
    if (_(d))
      return x(d);
    i = setTimeout(h, f(d));
  }
  function x(d) {
    return i = void 0, b && l ? m(d) : (l = s = void 0, r);
  }
  function C() {
    i !== void 0 && clearTimeout(i), p = 0, l = u = s = i = void 0;
  }
  function c() {
    return i === void 0 ? r : x(L());
  }
  function v() {
    var d = L(), w = _(d);
    if (l = arguments, s = this, u = d, w) {
      if (i === void 0)
        return E(u);
      if (a)
        return clearTimeout(i), i = setTimeout(h, t), m(u);
    }
    return i === void 0 && (i = setTimeout(h, t)), r;
  }
  return v.cancel = C, v.flush = c, v;
}
var Y = {
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
var ve = y, Ie = Symbol.for("react.element"), Se = Symbol.for("react.fragment"), Re = Object.prototype.hasOwnProperty, Oe = ve.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Te = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Q(e, t, o) {
  var l, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Re.call(t, l) && !Te.hasOwnProperty(l) && (s[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) s[l] === void 0 && (s[l] = t[l]);
  return {
    $$typeof: Ie,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Oe.current
  };
}
P.Fragment = Se;
P.jsx = Q;
P.jsxs = Q;
Y.exports = P;
var R = Y.exports;
const {
  SvelteComponent: ke,
  assign: z,
  binding_callbacks: B,
  check_outros: Pe,
  children: Z,
  claim_element: $,
  claim_space: Le,
  component_subscribe: G,
  compute_slots: Ne,
  create_slot: je,
  detach: I,
  element: ee,
  empty: K,
  exclude_internal_props: q,
  get_all_dirty_from_scope: Ae,
  get_slot_changes: We,
  group_outros: De,
  init: Fe,
  insert_hydration: T,
  safe_not_equal: Me,
  set_custom_element_data: te,
  space: Ue,
  transition_in: k,
  transition_out: W,
  update_slot_base: He
} = window.__gradio__svelte__internal, {
  beforeUpdate: ze,
  getContext: Be,
  onDestroy: Ge,
  setContext: Ke
} = window.__gradio__svelte__internal;
function V(e) {
  let t, o;
  const l = (
    /*#slots*/
    e[7].default
  ), s = je(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ee("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = $(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Z(t);
      s && s.l(r), r.forEach(I), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && He(
        s,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? We(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ae(
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
      W(s, n), o = !1;
    },
    d(n) {
      n && I(t), s && s.d(n), e[9](null);
    }
  };
}
function qe(e) {
  let t, o, l, s, n = (
    /*$$slots*/
    e[4].default && V(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), o = Ue(), n && n.c(), l = K(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Z(t).forEach(I), o = Le(r), n && n.l(r), l = K(), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      T(r, t, i), e[8](t), T(r, o, i), n && n.m(r, i), T(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && k(n, 1)) : (n = V(r), n.c(), k(n, 1), n.m(l.parentNode, l)) : n && (De(), W(n, 1, 1, () => {
        n = null;
      }), Pe());
    },
    i(r) {
      s || (k(n), s = !0);
    },
    o(r) {
      W(n), s = !1;
    },
    d(r) {
      r && (I(t), I(o), I(l)), e[8](null), n && n.d(r);
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
function Ve(e, t, o) {
  let l, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = Ne(n);
  let {
    svelteInit: u
  } = t;
  const p = O(J(t)), g = O();
  G(e, g, (c) => o(0, l = c));
  const a = O();
  G(e, a, (c) => o(1, s = c));
  const b = [], m = Be("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _
  } = ce() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: a,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(c) {
      b.push(c);
    }
  });
  Ke("$$ms-gr-react-wrapper", h), ze(() => {
    p.set(J(t));
  }), Ge(() => {
    b.forEach((c) => c());
  });
  function x(c) {
    B[c ? "unshift" : "push"](() => {
      l = c, g.set(l);
    });
  }
  function C(c) {
    B[c ? "unshift" : "push"](() => {
      s = c, a.set(s);
    });
  }
  return e.$$set = (c) => {
    o(17, t = z(z({}, t), q(c))), "svelteInit" in c && o(5, u = c.svelteInit), "$$scope" in c && o(6, r = c.$$scope);
  }, t = q(t), [l, s, g, a, i, u, r, n, x, C];
}
class Je extends ke {
  constructor(t) {
    super(), Fe(this, t, Ve, qe, Me, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, N = window.ms_globals.tree;
function Xe(e, t = {}) {
  function o(l) {
    const s = O(), n = new Je({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
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
          return u.nodes = [...u.nodes, i], X({
            createPortal: j,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== s), X({
              createPortal: j,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
const Ye = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Qe(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const l = e[o];
    return t[o] = Ze(o, l), t;
  }, {}) : {};
}
function Ze(e, t) {
  return typeof t == "number" && !Ye.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: i,
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
      type: i,
      useCapture: u
    }) => {
      o.addEventListener(i, r, u);
    });
  });
  const l = Array.from(e.childNodes);
  for (let s = 0; s < l.length; s++) {
    const n = l[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = D(n);
      t.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function $e(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const et = ne(({
  slot: e,
  clone: t,
  className: o,
  style: l,
  observeAttributes: s
}, n) => {
  const r = re(), [i, u] = oe([]), {
    forceClone: p
  } = ue(), g = p ? !0 : t;
  return se(() => {
    var E;
    if (!r.current || !e)
      return;
    let a = e;
    function b() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), $e(n, f), o && f.classList.add(...o.split(" ")), l) {
        const _ = Qe(l);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var C, c, v;
        (C = r.current) != null && C.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: h,
          clonedElement: x
        } = D(e);
        a = x, u(h), a.style.display = "contents", b(), (v = r.current) == null || v.appendChild(a);
      };
      f();
      const _ = Ce(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", b(), (E = r.current) == null || E.appendChild(a);
    return () => {
      var f, _;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((_ = r.current) == null || _.removeChild(a)), m == null || m.disconnect();
    };
  }, [e, g, o, l, n, s]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
}), {
  withItemsContextProvider: tt,
  useItems: nt,
  ItemHandler: ot
} = de("splitter.panels"), st = Xe(tt(["default"], ({
  children: e,
  ...t
}) => {
  const {
    items: {
      default: o
    }
  } = nt();
  return /* @__PURE__ */ R.jsxs(R.Fragment, {
    children: [/* @__PURE__ */ R.jsx("div", {
      style: {
        display: "none"
      },
      children: e
    }), o.length ? /* @__PURE__ */ R.jsx(M, {
      ...t,
      children: o == null ? void 0 : o.map((l, s) => {
        if (!l)
          return null;
        const {
          el: n,
          props: r
        } = l;
        return /* @__PURE__ */ le(M.Panel, {
          ...r,
          key: s
        }, n && /* @__PURE__ */ R.jsx(et, {
          slot: n
        }));
      })
    }) : null]
  });
}));
export {
  st as Splitter,
  st as default
};
